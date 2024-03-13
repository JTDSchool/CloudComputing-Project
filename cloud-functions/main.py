from flask import jsonify


def call_model(request):
    """
    Responds to a POST HTTP request.
    Reads 'text' from JSON body and returns it in the same format.

    Args:
        request (flask.Request): HTTP request object.

    Returns:
        The response text in JSON format, or an error status in JSON format.
    """
    # Ensure method is POST
    if request.method != "POST":
        return jsonify({"error": "Method not allowed"}), 405

    request_json = request.get_json(silent=True)

    if request_json and "text" in request_json:
        return jsonify({"text": request_json["text"]})
    else:
        return jsonify({"error": "No 'text' key found in JSON payload"}), 400
