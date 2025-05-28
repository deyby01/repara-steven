from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail 
from django.conf import settings

# Create your views here.
def homepage(request):
    return render(request, 'core/homepage.html')

def sobre_nosotros_view(request):
    return render(request, 'core/sobre_nosotros.html')

def contacto_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email_cliente = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            asunto = form.cleaned_data['asunto']
            mensaje_cliente = form.cleaned_data['mensaje']
            
            # ------ POR AHORA SOLO IMPRIMIREMOS EN CONSOLA ------#
            print("------ NUEVO MENSAJE ------")
            print(f"Nombre: {nombre}")
            print(f"Email: {email_cliente}")
            print(f"Teléfono: {telefono}")
            print(f"Asunto: {asunto}")
            print(f"Mensaje: {mensaje_cliente}")
            print("----------------------------")
            
            # --- Lógica para enviar email (la implementaremos después) ---
            # subject = f"Nuevo mensaje de contacto de {nombre}: {asunto}"
            # message_body = f"""
            # Has recibido un nuevo mensaje desde el formulario de contacto de ReparaSteven.cl:

            # Nombre: {nombre}
            # Email: {email_cliente}
            # Teléfono: {telefono if telefono else 'No proporcionado'}

            # Mensaje:
            # {mensaje_cliente}
            # """
            # from_email = settings.DEFAULT_FROM_EMAIL # O tu email configurado
            # recipient_list = [settings.EMAIL_HOST_USER] # El email de Steven o el email de la empresa

            # try:
            #     send_mail(subject, message_body, from_email, recipient_list)
            #     messages.success(request, '¡Tu mensaje ha sido enviado con éxito! Te contactaremos pronto.')
            # except Exception as e:
            #     print(f"Error al enviar email: {e}") # Para depuración
            #     messages.error(request, 'Hubo un error al enviar tu mensaje. Por favor, intenta más tarde o contáctanos directamente.')
            
            messages.success(request, '¡Mensaje recibido! (Simulacion). Te contactaremos pronto.')
            return redirect('core:contacto')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
            
    else:
        form = ContactForm()
        
    context = {
        'form': form 
    }
            
    return render(request, 'core/contacto.html', context)

def reparaciones_view(request):
    return render(request, 'core/reparaciones.html')