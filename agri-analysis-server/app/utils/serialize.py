def serialize(model):
    if isinstance(model, list):
        return [serialize(x) for x in model]

    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)
