
# see: https://github.com/PatrickPalmer/MayaCameraTools

import math
import maya.cmds as cmds

mm_to_inch = 0.03937007874

def compute_camera_viewing_frustum(camera, window_aspect, apply_overscan=False):
    """
    compute the position and the size of the rectangular viewing
    frustum in the near clipping plane.
    :Param str camera: camera name
    :Param float window_aspect: window aspect ratio
    :Returns tuple: (left, right, bottom, top)
    """
    
    film_aspect = cmds.camera(camera, query=True, aspectRatio=True)
    aperture_x = cmds.camera(camera, query=True, horizontalFilmAperture=True)
    aperture_y = cmds.camera(camera, query=True, verticalFilmAperture=True)
    offset_x = cmds.camera(camera, query=True, horizontalFilmOffset=True)
    offset_y = cmds.camera(camera, query=True, verticalFilmOffset=True)
    film_fit_offset = cmds.camera(camera, query=True, filmFitOffset=True)
    
    focal_len_inch = cmds.camera(camera, query=True, focalLength=True) * mm_to_inch
    focal_to_near = cmds.camera(camera, query=True, nearClipPlane=True) / focal_len_inch
    focal_to_near *= cmds.camera(camera, query=True, cameraScale=True)
    
    scale_x = 1.0
    scale_y = 1.0
    translate_x = 0.0
    translate_y = 0.0
    
    film_fit = cmds.camera(camera, query=True, filmFit=True)
    
    if film_fit == "fill":
        if window_aspect < film_aspect:
            scale_x = window_aspect / film_aspect
        else:
            scale_y = film_aspect / window_aspect

    elif film_fit == "horizontal":
        scale_y = film_aspect / window_aspect
        if scale_y > 1.0:
            translate_y = film_fit_offset * (aperture_y - (aperture_y * scale_y)) / 2.0
 
    elif film_fit == "vertical":
        scale_x = window_aspect / film_aspect
        if scale_x > 1.0:
            translate_x = film_fit_offset * (aperture_x - (aperture_x * scale_x)) / 2.0
            
    elif film_fit == "overscan":
        if window_aspect < film_aspect:
            scale_y = film_aspect / window_aspect 
        else:
            scale_x = window_aspect / film_aspect

    if apply_overscan:
        overscan = cmds.camera(camera, query=True, overscan=True)
        scale_x *= overscan
        scale_y *= overscan
    
    left   = focal_to_near * (-.5 * aperture_x * scale_x + offset_x + translate_x)
    right  = focal_to_near * ( .5 * aperture_x * scale_x + offset_x + translate_x)
    bottom = focal_to_near * (-.5 * aperture_y * scale_y + offset_y + translate_y)
    top    = focal_to_near * ( .5 * aperture_y * scale_y + offset_y + translate_y)
    
    return (left, right, bottom, top)


def get_camera_port_field_of_view(camera, port_width, port_height):
    """
    calculate the port field of view for the camera
    :Returns tuple: (horizontal_fov, vertical_fov) in radians
    """
    left, right, bottom, top = compute_camera_viewing_frustum(camera, float(port_width) / float(port_height))
    near = cmds.camera(camera, query=True, nearClipPlane=True)
    horizontal = math.atan(((right - left) * 0.5) / near) * 2.0
    vertical = math.atan(((top - bottom) * 0.5) / near) * 2.0
    return (horizontal, vertical)


def get_render_image_resolution():
    """
    get the rendering image resolution
    returns the width and height of the image to render (None if unable to retrieve)
    :Return tuple: (width, height)  
    """

    # get rendered image resolution by following the resolution attribute 
    # to the connected resolution node
    width = None
    height = None
    resolutions = cmds.listConnections('defaultRenderGlobals.resolution', s=True, d=False)
    if len(resolutions) > 0:
        width = cmds.getAttr(resolutions[0] + ".width")
        height = cmds.getAttr(resolutions[0] + ".height")
        
    return (width, height)


def will_render_ignore_film_gate():
    """ returns whether or not renders ignore the film gate """
    return cmds.getAttr('defaultRenderGlobals.ignoreFilmGate')


def get_camera_resolution_fov_ratio(camera):
    """ 
    get camera resolution and field of view
    :Param str camera: camera name
    :Return tuple: (camera_width, camera_height, fov_ratio)  
    """

    fov_ratio = 1.0

    # If a film gate is used this tells us whether the image is
    # blacked out in regions outside the film-fit region.
    # In our case we crop the image to the size of the region.
    ignore_film_gate = will_render_ignore_film_gate()

    # Resolution can change if camera film-gate clips image
    # so we must keep camera width/height separate from render
    # globals width/height.
    cam_width, cam_height = get_render_image_resolution()
    if not cam_width or not cam_height:
        cam_width = 320
        cam_height = 240

    # If we are using a film-gate then we may need to
    # adjust the resolution to simulate the 'letter-boxed' effect.

    aperture_x = cmds.camera(camera, query=True, horizontalFilmAperture=True)
    aperture_y = cmds.camera(camera, query=True, verticalFilmAperture=True)

    film_fit = cmds.camera(camera, query=True, filmFit=True)

    if film_fit == "horizontal":
        if not ignore_film_gate:
            new_height = cam_width / (aperture_x / aperture_y)
            if new_height < cam_height:
                cam_height = int(new_height)

        hfov, vfov = get_camera_port_field_of_view(camera, cam_width, cam_height)
        fov_ratio = hfov / vfov

    elif film_fit == "vertical":
        new_width = cam_height / (aperture_y / aperture_x)

        # case 1: film-gate smaller than resolution film-gate on
        if new_width < cam_width and not ignore_film_gate:
            cam_width = int(new_width)
            fov_ratio = 1.0

        # case 2: film-gate smaller than resolution film-gate off
        elif new_width < cam_width and ignore_film_gate:
            hfov, vfov = get_camera_port_field_of_view(camera, new_width, cam_height)
            fov_ratio = hfov / vfov

        # case 3: film-gate larger than resolution film-gate on
        elif not ignore_film_gate:
            hfov, vfov = get_camera_port_field_of_view(camera, new_width, cam_height)
            fov_ratio = hfov / vfov
		
        # case 4: film-gate larger than resolution film-gate off
        elif ignore_film_gate:
            hfov, vfov = get_camera_port_field_of_view(camera, new_width, cam_height)
            fov_ratio = hfov / vfov

    elif film_fit == "overscan":
        new_height = cam_width / (aperture_x / aperture_y)
        new_width = cam_height / (aperture_y / aperture_x)

        if new_width < cam_width:
            if not ignore_film_gate:
                cam_width = int(new_width)
                fov_ratio = 1.0
            else:
                hfov, vfov = get_camera_port_field_of_view(camera, new_width, cam_height)
                fov_ratio = hfov / vfov

        else:
            if not ignore_film_gate:
                cam_height = int(new_height)

            hfov, vfov = get_camera_port_field_of_view(camera, cam_width, cam_height)
            fov_ratio = hfov / vfov

    elif film_fit == "fill":
        new_width = cam_height / (aperture_y / aperture_x)

        if new_width >= cam_width:
            hfov, vfov = get_camera_port_field_of_view(camera, new_width, cam_height)
        else:
            hfov, vfov = get_camera_port_field_of_view(camera, cam_width, cam_height)

        fov_ratio = hfov / vfov


    return (cam_width, cam_height, fov_ratio)


def get_camera_field_of_view(camera):
    """ get camera field of view """
    cam_width, cam_height, fov_ratio = get_camera_resolution_fov_ratio(camera)
    return cmds.camera(camera, query=True, horizontalFieldOfView=True) / fov_ratio

 

def is_point_clipped(x, y, render_resolution, camera_resolution):
    """
    is a x,y point clipped out of the rendered image
    :Param x: x position
    :Param y: y position
    :Param tuple render_resolution: tuple of (render_width, render_height)
    :Param tuple camera_resolution: tuple of (camera_width, camera_height)
    :Return bool: True if clipped
    """
    clipped = False

    # if render_height != camera_height
    if render_resolution[1] != camera_resolution[1]:
        # new_height = (render_height - camera_height) / 2
        new_height = (render_resolution[1] - camera_resolution[1] ) / 2
        if y < new_height or y >= (render_resolution[1] - new_height):
            clipped = True

    # if render_width != camera_width
    if render_resolution[0] != camera_resolution[0]:
        # new_width = (render_width - camera_width) / 2
        new_width = (render_resolution[0] - camera_resolution[0] ) / 2
        if x < new_width or x >= (render_resolution[0] - new_width):
            clipped = True

    return clipped

