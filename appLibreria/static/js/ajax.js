window.onload = $(document).ready(function() {

   document.getElementById("fotoPagina").onmouseover = muestraMensaje;
   
   var pagina = document.getElementById("fotoPagina");
   href = '127.0.0.1:8000/appLibreria/comic/'
   $(pagina).qtip({
      content: {
         url: href,
         method: 'get'
      }
   });

  });