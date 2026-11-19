def alpha_blend(src_rgba, dest_rgba):
    src_alpha_factor = src_rgba[3] / 255.0
    dest_alpha_factor = (dest_rgba[3] / 255.0) * (1 - src_alpha_factor)
    result_alpha = src_alpha_factor + dest_alpha_factor
    if result_alpha == 0:
        return (0, 0, 0, 0)
    else:
        return(
            int(((src_rgba[0] * src_alpha_factor) + (dest_rgba[0] * dest_alpha_factor)) / result_alpha),
            int(((src_rgba[1] * src_alpha_factor) + (dest_rgba[1] * dest_alpha_factor)) / result_alpha),
            int(((src_rgba[2] * src_alpha_factor) + (dest_rgba[2] * dest_alpha_factor)) / result_alpha),
            int(result_alpha * 255)
        )