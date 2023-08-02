import tweepy

# Defina suas chaves e tokens da API do Twitter
consumer_key = 'SUA_CONSUMER_KEY'
consumer_secret = 'SUA_CONSUMER_SECRET'
access_token = 'SEU_ACCESS_TOKEN'
access_token_secret = 'SEU_ACCESS_TOKEN_SECRET'

# Autenticação com a API do Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Função para fazer um post
def fazer_post(tweet):
    api.update_status(tweet)
    print("Postagem realizada com sucesso!")


# Função para enviar uma mensagem direta
def enviar_mensagem(username, message):
    recipient = api.get_user(screen_name=username)
    recipient_id = recipient.id_str
    api.send_direct_message(recipient_id, text=message)
    print("Mensagem direta enviada com sucesso!")


# Exemplo de uso
if __name__ == "__main__":
    opcao = int(input("Escolha uma opção:\n1 - Fazer postagem\n2 - Enviar mensagem direta\nOpção: "))

    if opcao == 1:
        tweet = input("Digite o texto da postagem: ")
        fazer_post(tweet)
    elif opcao == 2:
        username = input("Digite o nome de usuário do destinatário: ")
        message = input("Digite a mensagem a ser enviada: ")
        enviar_mensagem(username, message)
    else:
        print("Opção inválida.")
