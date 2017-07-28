$(document).ready(function() {
  clearAttributes();

  // Class
  $('#id_char_class').keyup(function() {
    switch($('#id_char_class').val()) {
      case 'Barbarian':
      case 'barbarian':
        console.log("Barbarian chosen");
        break;
      case 'Bard':
      case 'bard':
        break;
      case 'Cleric':
      case 'cleric':
        break;
      case 'Druid':
      case 'druid':
        break;
      case 'Fighter':
      case 'fighter':
        break;
      case 'Monk':
      case 'monk':
        break;
      case 'Paladin':
      case 'paladin':
        break;
      case 'Ranger':
      case 'ranger':
        break;
      case 'Rogue':
      case 'rogue':
        break;
      case 'Sorcerer':
      case 'sorcerer':
        break;
      case 'Warlock':
      case 'warlock':
        break;
      case 'Wizard':
      case 'wizard':
        break;
    }
  });

  // Race
  $('#id_race').change(function() {
    switch($('#id_race').val()) {
      case 'Dwarf':
      case 'dwarf':
        clearAttributes();
        $('#id_constitution').val('2');
        break;
      case 'Elf':
      case 'elf':
        clearAttributes();
        $('#id_dexterity').val('2');
        break;
      case 'Halfling':
      case 'halfling':
        clearAttributes();
        $('#id_dexterity').val('2');
        break;
      case 'Human':
      case 'human':
        clearAttributes();
        $('#id_strength').val('1');
        $('#id_dexterity').val('1');
        $('#id_constitution').val('1');
        $('#id_intelligence').val('1');
        $('#id_wisdom').val('1');
        $('#id_charisma').val('1');
        break;
    }
  });

  // Randomize Button
  $('#randomize').click(function() {
    console.log('randomize clicked');
  });
});

function clearAttributes() {
  $('#id_strength').val('');
  $('#id_dexterity').val('');
  $('#id_constitution').val('');
  $('#id_intelligence').val('');
  $('#id_wisdom').val('');
  $('#id_charisma').val('');
}

// Class selection button click fix
$('#Barbarian_link').click(function() {
  console.log('Barbarian clicked');
  $('#Barbarian_tab').trigger('click');
});

$('#bard_link').click(function() {
  $('#bard_tab').trigger('click');
});

$('#cleric_link').click(function() {
  $('#_tab').trigger('click');
});

$('#cleric_link').click(function() {
  $('#_tab').trigger('click');
});

$('#druid_link').click(function() {
  $('#druid_tab').trigger('click');
});

$('#fighter_link').click(function() {
  $('#fighter_tab').trigger('click');
});

$('#monk_link').click(function() {
  $('#monk_tab').trigger('click');
});

$('#paladin_link').click(function() {
  $('#paladin_tab').trigger('click');
});

$('#ranger_link').click(function() {
  $('#ranger_tab').trigger('click');
});

$('#rogue_link').click(function() {
  $('#rogue_tab').trigger('click');
});

$('#sorcerer_link').click(function() {
  $('#sorcerer_tab').trigger('click');
});

$('#warlock_link').click(function() {
  $('#warlock_tab').trigger('click');
});

$('#wizard_link').click(function() {
  $('#wizard_tab').trigger('click');
});

// Race selection button fix
$('#dwarf_link').click(function() {
  $('#dwarf_tab').trigger('click');
});

$('#elf_link').click(function() {
  $('#elf_tab').trigger('click');
});

$('#halfling_link').click(function() {
  $('#halfling_tab').trigger('click');
});

$('#human_link').click(function() {
  $('#human_tab').trigger('click');
});

$('#dragonborn_link').click(function() {
  $('#dragonborn_tab').trigger('click');
});

$('#gnome_link').click(function() {
  $('#gnome_tab').trigger('click');
});

$('#half-elf_link').click(function() {
  $('#half-elf_tab').trigger('click');
});

$('#half-orc_link').click(function() {
  $('#half-orc_tab').trigger('click');
});

$('#tiefling_link').click(function() {
  $('#tiefling_tab').trigger('click');
});





$(document).ready(function() {
  console.log("Page is loaded");
  // classMenu();
  console.log("Class menu loaded");

  $('#Barbarian').click(function() {
    console.log("Barbarian fxn clicked");
    var oneObj = JSON.parse('\'' + '{{ Barbarian | escapejs }}');
    // $('#char_class').html(oneObj);
  });

  $('#Bard').click(function() {
    console.log("Bard was clicked");
  });

  $('#randomize').click(function() {
    console.log("Randomize clicked");
  });
});

function classMenu(classes) {
  // $('#char_class').html("");

  try{
    var arr = classes.results;
    var i = 0;
  }
  catch(err) {
    $('#char_class').html(err.message);
    $('#char_class').append('<br>{{ classes }}');
  }

  for(i = 0; i < classes.count; i++) {
    // $('#char_class').append("<button style='text-align: left;' class='col-xs-6 col-sm-6 col-md-6 col-lg-6'><div style='border: black solid 2px;' class='col-xs-6 col-sm-10 col-md-10 col-lg-10'><p style='padding: 10px 0;>'" + arr[i].name + "</p></div><div style='text-align: right; border: black solid 2px;' class='col-xs-2 col-sm-2 col-md-2  col-lg-2'><i class='material-icons'>keyboard_arrow_right</i></div></button>");
    $('#char_class').append("<a href='#" + arr[i].name + "' id=" + arr[i].name + "_link" + " style='text-align: center;' class='btn col-xs-6 col-sm-6 col-md-6 col-lg-6'>" + arr[i].name + "</a>");
    // $('#char_class').append("<button type='button' style='text-align: left;' class='col-xs-6 col-sm-6 col-md-6 col-lg-6'><div style='border: black solid 0; padding: 5px 0;' class='col-xs-6 col-sm-10 col-md-10 col-lg-10'></div><div style='text-align: right;' class='col-xs-2 col-sm-2 col-md-2  col-lg-2'><i class='material-icons'>keyboard_arrow_right</i></div></button>");
  }

  return;
}





var function_in_standalone_js = function(js_variable){
    classMenu(JSON.parse(js_variable));
};
