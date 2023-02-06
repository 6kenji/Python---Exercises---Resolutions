# Exemplo de redeclaracao da variavel globa; player score

player_score = 0
def update_player():
    global player_score
    result = 5
    if player_score < result:
        player_score = player_score + 1