
/* spusti serverStatus funkci po nacteni stranky */
window.onload = function() {
    call_nase_api();
};


//funkce ktera zavola nasi vlastni krasnou API a fetchne json
function call_nase_api(){
    fetch('/test')
	.then(res => res.json())
	.then(serverData => serverStatus(serverData))
}


//prepise data na hodnoty z jsonu
async function serverStatus(serverData){

    var serverName = document.getElementById('info1')
    serverName.innerHTML = serverData["server_name"]

    var serverStatus = document.getElementById('info2')
    serverStatus.innerHTML = 'status: ' + serverData['server_status']

    var playerCount = document.getElementById('info3')
    playerCount.innerHTML = 'players: ' + serverData['player_count_current']
    
    var serverIP = document.getElementById('info4')
    serverIP.innerHTML = 'IP: ' + serverData['server_ip']

    var mapaPic = document.getElementById("mapaPic");
    mapaPic.src = serverData['server_map'];

}
