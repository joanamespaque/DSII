$('.editar_pin').click(function() {
    let id =  $(this).attr('id');
    console.log("id: " + id);

    req = $.ajax({
        url: '/pin/buscar?id='+id,
        type: 'GET',
        async: true,
        cache: true
    });

    req.done(function(data) {
        let pin = JSON.parse(data.pin);
        console.log("pin: " + pin);
        console.log('pin titulo: ' + pin.titulo);
        $('#titulo').text("Título: " + pin.titulo);
        $('#descricao').text("Descrição: " + pin.descricao);
        $('#tematica').text("Temática: " + pin.tematica);
        $('#img_modal').attr("src", "/static/uploads/pins/" + pin.imagem);
    });
});
$('#list-tab a').on('click', function (e) {
    e.preventDefault()
    $(this).tab('show')
});
