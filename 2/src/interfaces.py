class ICanvas:
    def draw_lines(lines: List[GraphicsPoint]):
        """draws lines between i-th and (i-1)-th points"""
        pass


    def fill(lines: List[GraphicsPoint]):
        """fills all pixels in space closed by lines between i-th and (i-1)-th points"""
        pass


class IGraphicsItem:
    def paint(canvas: ICanvas):
        """paints this item onto canvas"""
        pass


class GraphicsLine(IGraphicsItem):
    start: GraphicsPoint
    end: GraphicsPoint


class GraphicsPoint(IGraphicsItem):
    x: int
    y: int


class GraphicsRect(IGraphicsItem):
    start: GraphicsPoint
    size: GraphicsPoint


class GraphicsEllipse(IGraphicsItem):
    rect: GraphicsRect


class GraphicsSquare(GraphicsRect):
    pass


class GraphicsCircle(GraphicsEllipse):
    pass


class GraphicsPolygon(IGraphiicsItem):
    pass


class QCanvas:
    canvas: QGraphicsScene
