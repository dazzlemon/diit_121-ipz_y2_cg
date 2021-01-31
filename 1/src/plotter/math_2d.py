from functools import reduce

def linear_map_2d(point, from_frame, to_frame):
    return (
        linear_map(point[0], (from_frame[0], from_frame[2]), (to_frame[0], to_frame[2])),
        linear_map(point[1], (from_frame[1], from_frame[3]), (to_frame[1], to_frame[3]))
    )


def linear_map(x, from_, to):
    return to[0] + (to[1] - to[0]) * ((x - from_[0]) / (from_[1] - from_[0]))


def points_frame(points):
    """
    in: [(x, y)]
    out: (minX, minY, maxX. maxY)
    """
    return reduce(
        lambda frame, point: (
            min(frame[0], point[0]),
            min(frame[1], point[1]),
            max(frame[2], point[0]),
            max(frame[3], point[1])
        ),
        points,
        (points[0][0], points[0][1], points[0][0], points[0][1])
    )


def widest_frame(r1, r2):
    return (
        min(r1[0], r2[0]),# minX
        min(r1[1], r2[1]),# minY
        max(r1[2], r2[2]),# maxX
        max(r1[3], r2[3]) # maxY
    )

