window.onload =  $(document).ready(function() {

   $('body > div.container > div.content > section.paginas > p').each(function () {
     var href = $(this).attr("href");
     href = '127.0.0.1:8000/appLibreria/comic/1/0'/
     $(this).qtip({
        content: {
           url: href,
           method: 'foto2'
        }
     });
   });
 });	
/** 
   document.getElementById("#fotoPagina").onmouseover = muestraMensaje;


   var pagina = document.getElementById("#fotoPagina");
   href = '127.0.0.1:8000/appLibreria/comic/1/0'
   $(pagina).qtip({
      content: {
         url: href,
         method: 'get'
      }
   });
*/