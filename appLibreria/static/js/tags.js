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
    }
}

function hideEverything(){
   if(! $('#Fantasia').hasClass('hide')){
    $('#Fantasia').addClass('hide');
   }
   if(! $('#Aventura').hasClass('hide')){
    $('#Aventura').addClass('hide');
   }
   if(! $('#Romantica ').hasClass('hide')){
    $('#Romantica ').addClass('hide');
   }
   if(! $('#Historica ').hasClass('hide')){
    $('#Historica ').addClass('hide');
   }
}