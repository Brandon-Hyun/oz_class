from marshmallow import Schema, fields

class BookSchema(Schema):
    # id 필드가 직렬홤( 즉, Python 객체에서 JSON으로 변환) 과정에서만 사용되고, (서버->클라이언트)
    # 역직렬화 (즉, JSON에서 Python 객체로 변환) 과정에서는 무시됨 (클라이언트->서버)
    # 즉, id는 서버에서 자동으로 관리되고, 클라이언트가 제공할 필요가 없음.
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)