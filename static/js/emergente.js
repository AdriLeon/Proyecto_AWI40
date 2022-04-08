(function($) {
    'use strict';
  
    var $activesystem1 = $('#freeze-system_1'),
      $processingsystem1 = $('#confirm-freeze-1'),
      $activesystem2 = $('#freeze-system_2'),
      $processingsystem2 = $('#confirm-freeze-2');
  
      $activesystem1.on('click', function() {
        $processingsystem1[0].showModal();
    });

        $activesystem2.on('click', function() {
        $processingsystem2[0].showModal();
    });
  
    $('#cancel1').on('click', function() {
        $processingsystem1[0].close();
    });

    $('#cancel2').on('click', function() {
        $processingsystem2[0].close();
    });
  
  })(jQuery);