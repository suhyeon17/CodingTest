def solution(players, callings):
	answer = []
	
	#선수&순위 저장{선수이름:현재 순위} *
	#player_rank = {"mumu":0, "soe":1, "poe":2, "kai":3, "mine":4}
	#rank_player = {0:"mumu", 1:"soe", 2:"poe", 3:"kai", 4:"mine"}

	player_rank = dict()
	rank_player = dict()
	for rank, player in enumerate(players):
		player_rank[player] = rank
		rank_player[rank] = player

	#{불리면 내 순위 -1 , 앞 사람 순위 +1}
	for call in callings:
		#불린 사람 앞 순위 사람
		before = rank_player[player_rank[call] -1] #poe
		#현재 불린 사람 순위
		rank = player_rank[call] #3

		#불린 사람 순위 -1
		player_rank[call] = rank - 1 # kai:2
		rank_player[rank - 1] = call #2:kai
		#불린 사람 앞 순위 +1
		player_rank[before] = rank #poe:3
		rank_player[rank] = before
		
	
	answer = list(rank_player.values())

	return answer