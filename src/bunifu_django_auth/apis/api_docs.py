from drf_spectacular.utils import extend_schema


def api_docs(  # noqa: PLR0913
    *,
    summary: str = "",
    description: str = "",
    tags: list[str] | None = None,
    request=None,
    responses=None,
    parameters=None,
    operation_id: str | None = None,
):
    """
    Centralized wrapper for drf-spectacular extend_schema.
    """

    return extend_schema(
        summary=summary,
        description=description,
        tags=tags or [],
        request=request,
        responses=responses,
        parameters=parameters,
        operation_id=operation_id,
    )


def get_docs(**kwargs):
    return api_docs(**kwargs)


def post_docs(**kwargs):
    return api_docs(**kwargs)


def put_docs(**kwargs):
    return api_docs(**kwargs)


def patch_docs(**kwargs):
    return api_docs(**kwargs)


def delete_docs(**kwargs):
    return api_docs(**kwargs)
