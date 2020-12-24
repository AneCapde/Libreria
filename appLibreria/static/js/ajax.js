window.onload = $(document).ready(function() {

      $('.texto ul li a').each(function () {
      var href = $(this).attr("href");
      var newUrl = href.replace(href, 'http://127.0.0.1:8000/appLibreria/comicsAjax/'+ $(this).attr('data-store')+ '/'); // Create new url
         $(this).qtip({
            content: {
               url: newUrl,
               method: 'get'
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