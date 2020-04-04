$('#username').keydown(function (e) {
    if (e.keyCode == 32) {
        return false;
    }
});
$('#email').keydown(function (e) {
    if (e.keyCode == 32) {
        return false;
    }
});
// alert("oi");
$(document).ready(function () {
    $(document).on('change', '.uploadFile :file', function () {
        var input = $(this),
            label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
        input.trigger('fileselect', [label]);
    });

    $('.uploadFile :file').on('fileselect', function (event, label) {

        var input = $(this).parents('.foto-change').find(':text'),
            log = label;

        if (input.length) {
            input.val(log);
        } else {
            if (log) alert(log);
        }

    });

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#img-profile').attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }

    $(".uploadFile ").change(function () {
        readURL(this);
    });
});
// $('#modal-perfil').on('hidden.bs.modal', function (e) {
//     alert("AAAAAAAAAAAAAAAAAAAAAAAAAAA");
// })
document.addEventListener('DOMContentLoaded', function () {
    setTimeout(function () {
        $(".msg").empty();
    }, 6000);
}, false);