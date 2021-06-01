$(document).ready(function()
{
    $('.cb_box').click(function()
    {
        var txt = "";
        $('.cb_box:checked').each(function()
        {
            txt += $(this).val()+","
        });
        txt = txt.substring(0, txt.length-1);
        $('#txt_values').val(txt);
    });
});
