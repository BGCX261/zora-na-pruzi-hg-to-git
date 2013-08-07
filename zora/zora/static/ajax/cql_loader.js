$(document).ready(function() {
    
    // vizuální kontrola na stránce da li je přítomno JQuery
    // ako ne, je tam zpráva
    $('#jquery_stav').remove();
    
	$('#cypher_skripty ul li a').click(function(){
        
		var obsah = $(this).attr('href');
		$('#obsah').hide('fast',nacitajObsah);
		$('#loader').remove();
		$('#hlavni').append('<span id="loader">Načitávam...</span>');
		$('#loader').fadeIn('normal');

		function nacitajObsah() {
			$('#obsah').load(obsah,'',pridajNovyObsah())
		}
		function pridajNovyObsah() {
			$('#obsah').show('normal',hideLoader());
		}
		function hideLoader() {
			$('#loader').fadeOut('normal');
		}

		return false;
	});
});
