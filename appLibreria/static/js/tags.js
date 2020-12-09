var seleccionados = [];

function updateResult(){
    seleccionados = [];
    hideEverything();
    $('#form_categorias :checked').each(function () { 
         seleccionados.push($(this).val());
    });
    if (seleccionados.length == 0){
        return;
    }else if (seleccionados.length == 1){
        var id = '#'+seleccionados[0];
        $(id).removeClass('hide');
    }else if (seleccionados.length == 2){
        var id = '#'+seleccionados[0]+seleccionados[1];
        $(id).removeClass('hide');
    }else{
        //solo filtramos hasta 2 selecciones
        return;
    }
}

function hideEverything(){
    $('#Fantasia').addClass('hide');
    $('#Aventura').addClass('hide');
    $('#Romantica').addClass('hide');
    $('#Historica').addClass('hide');
    $('#FantasiaAventura').addClass('hide');
    $('#FantasiaRomantica').addClass('hide');
    $('#FantasiaHistorica').addClass('hide');
    $('#AventuraRomantica ').addClass('hide');
    $('#AventuraHistorica').addClass('hide');
    $('#RomanticaHistorica').addClass('hide');
}