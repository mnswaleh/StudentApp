jQuery(document).ready(($) => {
  $(".apply-btn").click((e) => {
    $("#applicant").val($(e.currentTarget).data("val"));
  });

  $(".btn-cert").click((e) => {
    $.ajax({
      url: "/certificates",
      contentType: "application/json",
      type: "PUT",
      data: JSON.stringify({ certificate: $(e.currentTarget).data("val") }),
      success: function (result) {
        location.reload();
      },
    });
  });
});
