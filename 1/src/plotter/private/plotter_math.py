from functools import reduce
import numpy as np

__all__ = [
    "linear_map_2d",
    "linear_map",
    "intersections",
    "linspace_range",
    "frame",
    "line",
    "sqr_origin"
]

def linear_map_2d(point, from_frame, to_frame):
    return (
        linear_map(point[0], (from_frame[0], from_frame[2]), (to_frame[0], to_frame[2])),
        linear_map(point[1], (from_frame[1], from_frame[3]), (to_frame[1], to_frame[3]))
    )


def linear_map(x, from_, to):
    return to[0] + (to[1] - to[0]) * ((x - from_[0]) / (from_[1] - from_[0]))


def intersections(ps):
    return np.flatnonzero(np.diff(np.sign(ps)))


def linspace_range(range_, from_, step):
    ps0 = np.arange(from_ + step, range_[1], step)
    ps1 = np.arange(from_ - step, range_[0], -step)
    return np.concatenate((ps0, ps1))


def frame(arr3d):# [[[xs][ys]]]
    xys = np.transpose(arr3d, (1, 0, 2)).reshape((2, -1))# [0] - xs, [1] - ys
    return (
        np.min(xys[0]),
        np.min(xys[1]),
        np.max(xys[0]),
        np.max(xys[1])
    )

def line(center, length, orientation):
    if orientation == 0:
        start = (center[0], center[1] - length / 2)
        end = (center[0], center[1] + length / 2)
    elif orientation == 1:
        start = (center[0] - length / 2, center[1])
        end = (center[0] + length / 2, center[1])
    return (start[0], start[1], end[0], end[1])


def sqr_origin(center, size):
    return (
        center[0] - size / 2,
        center[1] - size / 2
    )

