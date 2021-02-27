
function ukazElement(jakej){

    var vsechnyElementy = document.getElementsByClassName('proAnim');

    for (var i = 0; i < vsechnyElementy.length; i++){
        if (vsechnyElementy[i].id != jakej){
            document.getElementById(vsechnyElementy[i].id).style.display = 'none';
        }
        else{
            document.getElementById(jakej).style.display = 'block';
        }
    }

}

/*

pro budouci generace

function mazatList(listClassek, moznost){
    for (var i = 0; i < listClassek.length; i++){
        listClassek[i].style.display = moznost;
    }
}

*/

