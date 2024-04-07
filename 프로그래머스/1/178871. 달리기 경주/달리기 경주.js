function solution(players, callings) {
    var answer = [...players];
    let playersData = {};
    const playerNumber = players.length;
    for (let i = 0; i < playerNumber; i++) {
        playersData[players[i]] = i;
    }
    for (let callPlayer of callings) {
        const num = playersData[callPlayer];
        let player1 = answer[num]
        let player2 = answer[num-1] 
        answer[num-1] = player1
        answer[num] = player2
        playersData[player1] = num - 1
        playersData[player2] = num
    }
    
    return answer;
}