import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from helpers.main import paginate_data, response_data

from .models import CRUDTestModel


# View to retrieve all the data
def get_all_data(request, *args, **kwargs):
    # initialize request_data dictionary
    request_data = {}
    # Check if there is body passed in the request
    if request.body:
        # Get request data
        request_data = json.loads(request.body)

    # Retrieve all data
    query_data = CRUDTestModel.objects.all()

    # Check if ordering is required
    if "order_by" in list(request_data.keys()):
        # Order by field passed in the request
        query_data = query_data.order_by(request_data.get("order_by"))

    # Convert to a list of objects
    data = list(query_data.values())

    # Return response
    return JsonResponse(
        response_data(
            status="success", detail="Data retrieved successfully", data=data
        ),
        safe=False,
    )


# View to retrieve all the data (paginated)
def get_all_data_paginated(request, *args, **kwargs):
    # initialize request_data dictionary
    request_data = {}
    # Check if there is body passed in the request
    if request.body:
        # Get request data
        request_data = json.loads(request.body)

    # Get current page number
    page_number = kwargs.get("page_number")
    # Retrieve all data
    query_data = CRUDTestModel.objects.all()

    if "order_by" in list(request_data.keys()):
        # Order by field passed in the request
        query_data = query_data.order_by(request_data.get("order_by"))

    # Convert to a list of objects
    data = list(query_data.values())
    # Paginate data
    resp_data = paginate_data(data, page_number, 10)

    # Return response
    return JsonResponse(resp_data, safe=False)


# View to retrieve only one data
def get_one_data(request, *args, **kwargs):
    # Retrieve specific data by specific attribute
    attr = kwargs.get("attr", None)  # Field to search by
    val = kwargs.get("val", None)  # Value to search by
    value_type = kwargs.get("value_type", None)  # Type of value to search

    # Type dicts
    types_dict = {
        "str": str,
        "int": int,
    }

    # Casted value
    casted_value = types_dict[value_type](val)

    query_param = {}
    # Set query parameters to a dictionary
    query_param[attr] = casted_value

    try:
        # Get query data by query param
        query_data = CRUDTestModel.objects.get(**query_param)

        # Convert query data to a dictionary
        data = query_data.to_dict()
        return JsonResponse(
            response_data(
                status="success", detail="Data retrieved successfully", data=data
            ),
            safe=False,
        )
    except CRUDTestModel.DoesNotExist:
        return JsonResponse(
            response_data(status="error", detail="Data does not exist"), safe=False
        )


# View to add data to the database
@csrf_exempt
def add_data(request, *args, **kwargs):
    if request.method == "POST":
        # Retrieve data from the request
        data = json.loads(request.body)
        try:
            # model data
            db_data = CRUDTestModel.objects.create(**data)

            # Convert database data to a dictionary
            resp_data = db_data.to_dict()

            return JsonResponse(
                response_data(
                    status="success", detail="Data added successfully", data=resp_data
                ),
                safe=False,
            )
        except Exception:
            return JsonResponse(
                response_data(
                    status="error",
                    detail="Encountered an error during data creation",
                ),
                safe=False,
            )

    return JsonResponse(
        response_data(
            status="error",
            detail="Method is not allowed",
        ),
        safe=False,
    )


# View to update data
@csrf_exempt
def update_data(request, *args, **kwargs):
    if request.method == "PATCH":
        # Get id of data
        data_id = kwargs.get("data_id")

        # Request data
        data = json.loads(request.body)

        # Update data by Id
        try:
            # Filter db by id and update data
            CRUDTestModel.objects.filter(id=data_id).update(**data)

            # Retrieve updated data
            test_model = CRUDTestModel.objects.get(id=data_id)
            return JsonResponse(
                response_data(
                    status="error", detail="Data not found", data=test_model.to_dict()
                ),
                safe=False,
            )
        except CRUDTestModel.DoesNotExist:
            return JsonResponse(
                response_data(
                    status="error",
                    detail="Data not found",
                ),
                safe=False,
            )

    return JsonResponse(
        response_data(
            status="error",
            detail="Method is not allowed",
        ),
        safe=False,
    )


# View to delete a data
@csrf_exempt
def delete_data(request, *args, **kwargs):
    if request.method == "DELETE":
        # Get data id from request
        data_id = kwargs.get("data_id")
        try:
            # Retrieve data from database
            db_data = CRUDTestModel.objects.get(id=data_id)

            # Delete data from database
            db_data.delete()

            # Return response
            return JsonResponse(
                response_data(
                    status="error",
                    detail="Data deleted successfully",
                ),
                safe=False,
            )
        except CRUDTestModel.DoesNotExist:
            return JsonResponse(
                response_data(
                    status="error",
                    detail="Data not found",
                ),
                safe=False,
            )

    return JsonResponse(
        response_data(
            status="error",
            detail="Method is not allowed",
        ),
        safe=False,
    )


# View to delete multiple data
@csrf_exempt
def delete_many_data(request, *args, **kwargs):
    if request.method == "POST":
        # Data ids to be deleted
        data_ids = json.loads(request.body).get("data_ids")

        # Keep track of errors
        deletion_errors = {}

        # Loop through the data to delete
        for data_id in data_ids:
            try:
                # Retrieve data from database
                db_data = CRUDTestModel.objects.get(id=data_id)

                # Delete data from database
                db_data.delete()

            except CRUDTestModel.DoesNotExist:
                # Set error message when data is not found
                deletion_errors[data_id] = "Deletion failed"

        error_length = len(list(deletion_errors.keys()))

        resp_data = {"status": "success", "detail": "Data deleted successfully"}

        # there are errors
        if error_length:
            resp_data["status"] = "error"
            resp_data["detail"] = "Failed to delete some data"
            resp_data["errors"] = deletion_errors

        # Return response
        return JsonResponse(
            response_data(**resp_data),
            safe=False,
        )

    return JsonResponse(
        response_data(
            status="error",
            detail="Method is not allowed",
        ),
        safe=False,
    )
