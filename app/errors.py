# app/errors.py
from flask import render_template, request, jsonify
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
	if request.accept_mimetypes.accept_json and \
	not request.accept_mimetypes.accept_html:
		response = jsonify( {'error': 'Nicht gefunden'} )
		response.status_code = 404
		return response
	else:
		return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
	db.session.rollback()
	if request.accept_mimetypes.accept_json and \
	not request.accept_mimetypes.accept_html:
		response = jsonify( {'error': 'Interner Server Error'} )
		response.status_code = 500
		return response
	return render_template('500.html'),500
