from flask import Flask, Blueprint, render_template, request, redirect, url_for, current_app
import sendgrid
from sendgrid.helpers.mail import Email, Mail, To

# Definición del Blueprint
bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')

@bp.route('/mail', methods=['GET', 'POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('correo')
    mensaje = request.form.get('mensaje') 
    if request.method == 'POST':
        send_email(name, email, mensaje)
        return render_template('portfolio/sent_mail.html')
    return redirect(url_for('portfolio.index'))

def send_email(name, email, mensaje):
    mi_email = 'jorgen.granda2@ute.edu.ec'
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
    from_email = Email(mi_email)
    to_email = To(mi_email, substitutions={
        "-name-": name,
        "-email-": email,
        "-mensaje-": mensaje,
    })
    html_content = f"""
        <p>Hola Nicolas, recibiste un contacto de:</p>
        <p>Nombre: {name} </p>
        <p>Email: {email} </p>
        <p>Mensaje: {mensaje} </p>
    """
    mail = Mail(from_email, to_email, 'Nuevo contacto desde la web', html_content=html_content)
    response = sg.client.mail.send.post(request_body=mail.get())


