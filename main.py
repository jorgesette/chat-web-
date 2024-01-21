
# Botao de inicar o chat
    #popup 
        # Bem vindo ao chat
        # Escreva seu nome
        # Entrar no chat


# Chat 
    # Gabriel entrou no chat
    # Mensagens do usuario
# Campo para digitar msg
# Botao de enviar

import flet as ft

def main(pagina):
    texto = ft.Text('Chat Online') 


    nome_usuario = ft.TextField(label='Escreva seu nome')

    chat = ft.Column()

    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
        

    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(evento):
        # Colocar o nome do usuario na mensagem
        texto_campo_mensagem = f'{nome_usuario.value}: {campo_mensagem.value}'        


        pagina.pubsub.send_all(texto_campo_mensagem)
        # Limpar o campo mensagem
        campo_mensagem.value = ''

        pagina.update()

    campo_mensagem = ft.TextField(label='Escreva sua mensagem aqui', on_submit=enviar_mensagem)

    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)


    def entrar_chat(evento):
        # feche o popup
        popup.open = False

        # Tire o botao iniciar chat da tela
        pagina.remove(botao_inicar)
        # Adicionar o CHAT
        pagina.add(chat)
        # criar o campo de enviar mensagem
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)
        # botao de enviar mensagem

        texto = f'{nome_usuario.value} entrou no chat!'
        pagina.pubsub.send_all(texto)
        pagina.update()


    popup = ft.AlertDialog(

        open = False,
        modal = True,
        title = ft.Text('Bem vindo ao Chat Online'),
        content =  nome_usuario,
        actions = [ft.ElevatedButton('Entrar', on_click=entrar_chat)]
    )


    def iniciar_chat(evento):   # sempre um evento no on_click
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_inicar = ft.ElevatedButton('Iniciar Chat', on_click= iniciar_chat)



    pagina.add(texto)
    pagina.add(botao_inicar)


# ft.app(main)

ft.app(main, view=ft.WEB_BROWSER)