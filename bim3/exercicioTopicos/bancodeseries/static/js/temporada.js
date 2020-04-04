$( "#serie" ).change(function() {
    if( $(this).val() ) {
        let cod =  $(this).val();
        let temporada = $("#temporada");
        $.ajax({
            url: '/episodio/listaTemporadas?cod='+cod,
            type: 'GET',
            async: true
        }).done(function(data){
            let json = JSON.parse(data.temporadas);
            let count = Object.keys(json).length;
            if(count>0){
                for(i = 0; i < count; i++){
                    temporada.append($('<option>').val(json[i].cod).text(json[i].titulo));
                }
            } else{
                temporada.empty()
                $('div.msg h4').text("Essa série ainda não possui temporadas cadastradas.")
                setTimeout(function() {
                    $('div.msg h4').text("");
                }, 4000);
            }
        });
    }
});