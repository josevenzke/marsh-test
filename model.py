from marshmallow import Schema, fields, validate, validates, ValidationError
from datetime import datetime
import uuid

def validate_scope(scope):
    if scope != "teste":
        raise ValidationError('Scope doesnt exist')

class CreateCredSchema(Schema):
    client_id = fields.UUID(load_default=uuid.uuid4)
    scopes = fields.List(fields.String(validate=validate_scope), required=True)
    issuer_id = fields.String(validate=validate.Length(min=5), required=True)
    created_at = fields.DateTime(load_default=datetime.utcnow(), load_only=True)



class UpdateCredSchema(Schema):
    scopes = fields.List(fields.String(), required=True)
    issuer_id = fields.String(validate=validate.Length(min=5), required=True)