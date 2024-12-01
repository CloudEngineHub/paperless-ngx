from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema


class AngularApiAuthenticationOverrideScheme(OpenApiAuthenticationExtension):
    target_class = "paperless.auth.AngularApiAuthenticationOverride"
    name = "AngularApiAuthenticationOverride"

    def get_security_definition(self, auto_schema):
        return {
            "name": "Angular Authorization",
            "description": "Automatic Angular authentication for the dev server",
        }


def generate_object_with_permissions_schema(serializer_class):
    return {
        operation: extend_schema(
            parameters=[
                OpenApiParameter(
                    name="full_perms",
                    type=OpenApiTypes.BOOL,
                    location=OpenApiParameter.QUERY,
                ),
            ],
            responses={
                200: serializer_class(many=operation == "list", all_fields=True),
            },
        )
        for operation in ["list", "retrieve"]
    }
