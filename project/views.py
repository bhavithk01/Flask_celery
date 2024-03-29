from flask import Blueprint, jsonify

from .tasks import process_file

main = Blueprint('main', __name__)

@main.route('/procee-file', methods=['GET', 'POST'])
def create_user():
    # Calling background task
    process_file.delay()
    return jsonify("Completed")