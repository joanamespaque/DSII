$('#seta').click(function() {
    let duracao =  $(this).attr('f_duracao');
    let sinopse = $(this).attr('f_sinopse');
    let elenco = $(this).attr('f_elenco');
    let dataLancamento = $(this).attr('f_dataLancamento');
    let classificacao = $(this).attr('f_classificacao');
    let div = $('#response');
    $ajax({
        url: '/buscar',
        type: 'POST',
        async: true,
        data: {duracao : duracao, sinopse : sinopse, elenco : elenco, dataLancamento: dataLancamento, classificacao : classificacao}
    }).done(function(data) {
        let count = Object.keys(data).length;
        for(i = 0; i < count; i++){
            td = document.createElement("TD");
            td.text(Object.values(data)[i])
            div.appendChild(td);
        }
        // console.log(data);
        $('#response').append(data);
    });
});

