from api.redirects import blueprint
from flask import redirect, url_for

@blueprint.route('/')
def redirect_to_website():
    return redirect(url_for('site_bp.index'))