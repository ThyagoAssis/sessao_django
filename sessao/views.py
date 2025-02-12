#Imporetar o Redirect
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if 'nome_usuario' not in request.session:
        return redirect('login')
    else:
        return render(request,'home.html')
       

#Cria as sessoes
def solicitar_dados(request):
    #Verifica se clicou no botao do formulario
    if request.method == "POST":

        #captura os dados do formulario e guarda em um varivavel
        nome_usuario = request.POST.get("nome_usuario")
        email = request.POST.get("email")
        
        # Armazenando os dados na sessão
        request.session["nome_usuario"] = nome_usuario
        request.session["email"] = email
        
        return redirect("inicio")
    
    return render(request, "section.html")

def encerrar_sessao(request):
    request.session.flush()  # Remove todos os dados da sessão e exclui a sessão
    return redirect("/")  # Redireciona para a página inicial ou qualquer outra página