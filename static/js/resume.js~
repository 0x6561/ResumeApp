//<!--     DISPLAY RESUME    -->
$(document).ready(function(){
  $.ajax({
    type: 'GET',
    // This is the type of data you're expecting back from the server.
    dataType: 'json',
    url: 'get',
    success: function (resume_json) {
      console.log('sucess!, resume loaded');
      //display_resume(resume_json);
      add_edit_flds(resume_json);
    }
  });
});

//<!--     DISPLAY RESUME -->
function display_resume(resume, preview=false){
  clear_resume();
  $('#NAME_DIV').html(resume.name); 
  $('#LOCATION_DIV').html(resume.location);
  if('email' in resume) $('#EMAIL_DIV').html('<a href="mailto:' + resume.email+ '">' + resume.email+ '</a>');
  if('website' in resume) $('#WEBSITE_DIV').html('<a href="'+resume.website + '">' + resume.website + '</a>');
  if('github' in resume) $('#GITHUB_DIV').html('<a href="'+resume.github + '">' + resume.github + '</a>');
  if('linkedin' in resume) $('#LINKEDIN_DIV').html('<a href="'+resume.linkedin + '">' + resume.linkedin + '</a>');

  //EDUCATION
  $.each(resume.Education, function(index, degree){
    $('#EDUCATION_DIV').append('<div class="row text-white">' + degree.degree + ' - ' + degree.Institution + '</div>');
    if((['Cumulative GPA'] in degree )&&( degree['Cumulative GPA'] != 'undefined'))$('#EDUCATION_DIV').append('<div class="row"><li>Cumulative GPA: ' + degree['Cumulative GPA'] + '</li></div>');
  });

  //KNOWLEDGE
  $.each(resume.Knowledge, function(index, knowledge){
    $('#KNOWLEDGE_DIV').append('<div class="text-white col">' + knowledge + '</div>');
  });

  //Programming Languages
  $.each(resume['Programming Languages'], function(index, language){
    $('#LANGUAGES_DIV').append('<div class="text-white col">' + language + '</div>');
  });

  //Frameworks
  $.each(resume.Frameworks, function(index, framework){
    $('#FRAMEWORKS_DIV').append('<div class="text-white col">' + framework + '</div>');
  });

  //Database
  $.each(resume.Database, function(index, dbtype){
    var index_class = index.replace(/[(){}]/g,'');//remove parenthesis/braces
    index_class = index_class.replace(/ /g,'__');//replace spaces with underscores
    var dbkind = '<div class="container DB-TYPE"><div class="container row border-bottom h6 text-white DB-TYPE-TITLE">' + index + '</div>';
    dbkind += '<div id="' + index_class + '" class="container row border-info text-white"></div><br id="foo"></div>';
    $('#DATABASE_DIV').append(dbkind);
    $.each(resume.Database[index], function(index, db){
      var dbase = '<div class="col text-white DB-TYPE-INSTANCE">' + db + '</div>';
      $('#'+index_class).append(dbase);
    });
  });

  //Operating Systems
  $.each(resume['Operating Systems'], function(index, os){
    $('#OS_DIV').append('<div class="text-white col">' + os + '</div>');
  });

  //Class Projects
  $.each(resume['Class Projects'], function(index, cproj){
    $('#CPROJ_DIV').append('<div class="row text-white"><li>' + cproj + '</li></div>');
  });

  //Research
  $.each(resume['Research'], function(index, rsch){
    $('#RSCH_DIV').append('<div class="row text-white"><li>' + rsch + '</li></div>');
  });

  //Personal Projects
  $.each(resume['Personal Projects'], function(index, pproj){
    $('#PPROJ_DIV').append('<div class="row text-white"><li>' + pproj + '</li></div>');
  });

  //WORK HISTORY
  $.each(resume['Work Experience'], function(index, job){
    var position = '<div class="row container">';
    position += '<div class="w-25">';
    position += '<div class="container row text-white">Employer: ' + job.Employer + '</div>';
    position += '<div class="container row text-white">Title: ' + job.Position + '</div>';
    position += '<div class="container row text-white">from: ' + job.from + '  to: ' + job.to + '</div>';
    position += '</div>';
    position += '<div class="w-75">';
    position += '<div class="container row text-white">Duties: <br>' + job.Duties + '</div>';
    position += '</div>';
    position += '</div>';
    $('#WORK_DIV').append(position);
  });

}//close display_resume

//clears each section of resume scaffold 
// (to add editing elements)
function clear_resume(){
  $(".FLD").each(function(){
    $(this).empty();
  });
  $(".E_BTN").each(function(){
    $(this).remove();
  });
}

//<!--     ADD EDIT LOGIC  -->
// all remove buttons use this
$(document).on("click", ".remove_button", function(){
    $(this).parent().remove();
});

function add_edit_btns(){
  $('#EDUCATION_SECTION_DIV').append('<div id="EDUCATION_DIV_BTN" class="row E_BTN"><button class="btn btn-success" type="button" onclick="add_degree()">Add Degree</button></div>');
  $('#KNOWLEDGE_SECTION_DIV').append('<div id="KNOWLEDGE_DIV_BTN" class="container row E_BTN"><button class="btn btn-success" type="button" onclick="add_knowledge()">Add Knowledge</button></div>');
  $('#PROGRAMMING_LANGUAGE_DIV').append('<div id="LANGUAGES_DIV_BTN" class="container row E_BTN"><button class="btn btn-success" type="button" onclick="add_language()">Add Programming Languages</button></div>');
  $('#FRAMEWORKS_SECTION_DIV').append('<div id="FRAMEWORKS_DIV_BTN" class="container row E_BTN"><button class="btn btn-success" type="button" onclick="add_framework()">Add Frameworks</button></div>');
  $('#DATABASES_SECTION_DIV').append('<div id="DATABASE_DIV_BTN" class="container row E_BTN"><button class="btn btn-success" type="button" onclick="add_db_type()">Add Database Type</button></div>');
  $('#OPERATING_SYSTEMS_DIV').append('<div id="OS_DIV_BTN" class="container row E_BTN"><button class="btn btn-success" type="button" onclick="add_os()">Add Operating Systems</button></div>');
  $('#CLASS_PROJECTS_DIV').append('<div id="CPROJ_DIV_BTN" class="container row E_BTN"><button class="btn btn-success" type="button" onclick="add_cproj()">Add Class Project</button></div>');
  $('#RESEARCH_DIV').append('<div id="RSCH_DIV_BTN EDIT_BTN" class="container row E_BTN"><button class="btn btn-success" type="button" onclick="add_rsch()">Add Research</button></div>');
  $('#PPROJ_SECTION_DIV').append('<div id="PPROJ_DIV_BTN" class="container row E_BTN"><button class="btn btn-success" type="button" onclick="add_pproj()">Add Personal Project</button></div>');
  $('#EMPLOYMENT_DIV').append('<div id="WORK_DIV_BTN" class="container row E_BTN"><button class="btn btn-success" type="button" onclick="add_job()">Add Job</button></div>');
  $('#END').append('<div id="PREVIEW_DIV_BTN" class="container row E_BTN"><button class="btn-lg btn-success" type="button" onclick="save()">PREVIEW RESUME</button></div>');
}

function add_edit_flds(resume={}){
clear_resume();
  add_edit_btns();
  add_top_section(resume);
  //add degrees
  $.each(resume.Education, function(index, degree){
    add_degree(degree);
  });
  //add Knowledge
  $.each(resume.Knowledge, function(index, knowledge){
    add_knowledge(knowledge);
  });
  //add Programming Languages
  $.each(resume['Programming Languages'], function(index, language){
    add_language(language);
  });
  //add Frameworks
  $.each(resume.Frameworks, function(index, framework){
    add_framework(framework);
  });
  //add Database
  $.each(resume.Database, function(index, dbtype){
    var tgt = add_db_type(index);
    $.each(resume.Database[index], function(index, db){
      add_db_instance(db, tgt);
    });
  });
  //Operating Systems
  $.each(resume['Operating Systems'], function(index, os){
    add_os(os);
  });
  //Class Projects
  $.each(resume['Class Projects'], function(index, cproj){
    add_cproj(cproj);
  });
  //Research
  $.each(resume['Research'], function(index, rsch){
    add_rsch(rsch);
  });
  //Personal Projects
  $.each(resume['Personal Projects'], function(index, pproj){
    add_pproj(pproj);
  });
  //WORK HISTORY
  $.each(resume['Work Experience'], function(index, jb){
    add_job(jb);
  });

}

function add_top_section(resume = {'name': 'Name', 'location': 'Location', 'email': 'email', 'website': 'Website', 'github': 'GitHub', 'linkedin': 'Linkedin'}){
  $('#TOP_DIV').html("Date Modified: " + resume.date_modified);
  var name_fld = '<div class="form-inline"><label class="control-label" for="name">Name</label>';
  name_fld += '<input type="text" class="form-control" id="NAME" aria-describedby="name" value="' + resume.name + '"></div>';
  $('#NAME_DIV').prepend(name_fld);

  var location_fld = '<div class="form-inline"><label class="control-label" for="location">Location</label>';
  location_fld += '<input type="text" class="form-control" id="LOCATION" aria-describedby="name" value="' + resume.location + '"></div>';
  $('#LOCATION_DIV').prepend(location_fld);

  var email_fld = '<label class="control-label" for="email">Email</label>';
  email_fld += '<input type="text" class="form-control" id="EMAIL" aria-describedby="email" value="' + resume.email + '">';
  $('#EMAIL_DIV').prepend(email_fld);

  var website_fld = '<label class="control-label" for="website">Website</label>';
  website_fld += '<input type="text" class="form-control" id="WEBSITE" aria-describedby="website" value="' + resume.website + '">';
  $('#WEBSITE_DIV').prepend(website_fld);

  var github_fld = '<label class="control-label" for="github">Github</label>';
  github_fld += '<input type="text" class="form-control" id="GITHUB" aria-describedby="github" value="' + resume.github + '">';
  $('#GITHUB_DIV').prepend(github_fld);

  var linkedin_fld = '<label class="control-label" for="linkedin">LinkedIn</label>';
  linkedin_fld += '<input type="text" class="form-control" id="LINKEDIN" aria-describedby="linkedin" value="' + resume.linkedin + '">';
  $('#LINKEDIN_DIV').prepend(linkedin_fld);
}

// add degrees
var degree_ctr = 0;
function add_degree(deg={degree:'degree',Institution: "institution",GPA:"GPA"}){
  var degree = '<div class="container text-white border form-inline DEGREE">'; 
  degree += '<label class="control-label" for="degree-' + degree_ctr + '">Degree: </label>';
  degree += '<input type="text" class="form-control DEGREE_DEGREE" id="degree-' + degree_ctr + '" aria-describedby="degree" value="' + deg.degree + '">';
  degree += '<label class="control-label" for="institution-' + degree_ctr + '">Institution: </label>';
  degree += '<input type="text" class="form-control DEGREE_INSTITUTION" id="institution-' + degree_ctr + '" aria-describedby="institution" value="' + deg.Institution + '">';
  degree += '<label class="control-label" for="cgpa-' + degree_ctr + '">Cumulative GPA: </label>';
  degree += '<input type="text" class="form-control DEGREE_GPA" id="cgpa-' + degree_ctr + '" aria-describedby="gpa" value="' + deg['Cumulative GPA']+ '">';
  degree +=  '<button class="btn btn-danger row remove_button" type="button">Remove</button>';
  degree +=  '</div>';
  $('#EDUCATION_DIV').append(degree);
  degree_ctr += 1;
}

// add knowledge
function add_knowledge(kn = "knowledge"){
  var knowledge = '<div class="container row form-inline">';
  knowledge += '<input type="text" class="form-control w-75 KNOWLEDGE_SKILL" aria-describedby="knowledge" value="' + kn + '">';
  knowledge += '<button class="btn form-control btn-danger remove_button" type="button">Remove</button></div>';
  $('#KNOWLEDGE_DIV').append(knowledge);
}

//add language
function add_language(lang='Programming Language'){
  var language =  '<div class="form-inline container row">';
  language += '<input type="text" class="form-control w-75 PROGRAMMING_LANGUAGE" aria-describedby="language" value="' + lang + '">';
  language += '<button class="btn form-control btn-danger remove_button" type="button">Remove</button></div>';
  $('#LANGUAGES_DIV').append(language);
}

//add framework
function add_framework(frmwk = 'Framework'){
  var framework =  '<div class="form-inline container row">';
  framework += '<input type="text" class="form-control w-75 FRAMEWORK" aria-describedby="framework" value="' + frmwk + '">';
  framework += '<button class="btn form-control btn-danger remove_button" type="button">Remove</button></div>';
  $('#FRAMEWORKS_DIV').append(framework);
}

var dbt_ctr = 0;
function add_db_type(db='Database Type'){
  var db_type = db.replace(/[(){}]/g,'');//remove parenthesis/braces
  db_type = db_type.replace(/ /g,'__');//replace spaces with underscores
  var dbt_id = db_type + dbt_ctr; 
  var dbtype = '<div data-id="' + dbt_id + '" class="container row form-inline border-top">';
  dbtype += '<label class="control-label" for="db-' + dbt_id + '">Database Type</label>';
  dbtype += '<input data-id="' + dbt_id + '" id="db-' + dbt_id + '" type="text" class="form-control w-75 DBTYPE"';
  dbtype += ' aria-describedby="database type" value="' + db + '">';
  dbtype += '<button class="btn form-control btn-danger remove_button" type="button">-</button>';
  dbtype += '<button class="btn form-control btn-success add_new_db_instance" type="button" >+</button><div id="' + dbt_id + '" class="row container w-50 border-bottom"></div></div>';
  $('#DATABASE_DIV').append(dbtype);
  dbt_ctr += 1;
  return dbt_id;
}

function add_db_instance(db='Database', target='DATABASE_DIV'){
  var dbtype_i =  '<div class="container row form-inline">';
  dbtype_i += '<input type="text" class="form-control w-75 DBTYPE_INSTANCE ' + target +'"';
  dbtype_i += ' aria-describedby="database type" value="' + db + '">';
  dbtype_i += '<button class="btn form-control btn-danger remove_button" type="button">-</button></div>';
  $('#'+target).append(dbtype_i);
}

//for adding databases
$(document).on("click", ".add_new_db_instance", function(){
  var target = $(this).parent().attr('data-id');
  add_db_instance('Database',target);
});

function add_os( os = 'Operating System'){
  var os_div =  '<div class="form-inline container row">';
  os_div += '<input type="text" class="form-control w-75 OS" aria-describedby="os" value="' + os + '">';
  os_div += '<button class="btn form-control btn-danger remove_button" type="button">Remove</button></div>';
  $('#OS_DIV').append(os_div);
}

function add_cproj(cproj = 'Class Proj'  ){
  var cproj_div  =  '<div class="form-inline container row">';
  cproj_div += '<input type="text" class="form-control w-75 CPROJ" aria-describedby="cproj" value="' + cproj + '">';
  cproj_div += '<button class="btn form-control btn-danger remove_button" type="button">Remove</button></div>';
  $('#CPROJ_DIV').append(cproj_div);
}

function add_rsch(rsch = "Research"){
  var rsch_div =  '<div class="form-inline container row">';
  rsch_div += '<input type="text" class="form-control w-75 RSCH" aria-describedby="rsch" value="' + rsch + '">';
  rsch_div += '<button class="btn form-control btn-danger remove_button" type="button">Remove</button></div>';
  $('#RSCH_DIV').append(rsch_div);
}

function add_pproj( pproj = 'Personal Project'){
  var pproj_div =  '<div class="form-inline container row">';
  pproj_div += '<input type="text" class="form-control w-75 PPROJ" aria-describedby="pproj" value="' + pproj + '">';
  pproj_div += '<button class="btn form-control btn-danger remove_button" type="button">Remove</button></div>';
  $('#PPROJ_DIV').append(pproj_div);
}

var job_ctr = 0;
function add_job(job={'Employer':'Employer','from':'From','to':'To','Position':'Job Title','Duties':'Job Duties'}){
  var job_div = '<div class="row form-inline border-secondary WORK_HISTORY">';
  job_div += '<label class="control-label" for="job-' + job_ctr + '">Employer</label>';
  job_div += '<input type="text" class="form-control JOB_EMPLOYER" id="job-' + job_ctr + '" aria-describedby="Employer" value="' + job.Employer + '">';
  job_div += '<label class="control-label" for="from-' + job_ctr + '">From</label>';
  job_div += '     <input type="text" class="form-control JOB_FROM " id="from-' + job_ctr + '" aria-describedby="from" value="' + job.from + '">';
  job_div += '<label class="control-label" for="to-' + job_ctr + '">To</label>';
  job_div += '<input type="text" class="form-control JOB_TO" id="to-' + job_ctr + '" aria-describedby="to" value="' + job.to + '">';
  job_div += '<label class="control-label" for="title-' + job_ctr + '">Title</label>';
  job_div += '<input type="text" class="form-control JOB-TITLE" id="title-' + job_ctr + '" aria-describedby="title" value="'+ job.Position +'">';
  job_div += '<label class="control-label" for="duties-' + job_ctr + '">Duties</label>';
  job_div += '<textarea class="form-control w-75 JOB_DUTIES" name="duties-' + job_ctr + '" aria-describedby="duties">' + job.Duties + '</textarea>';
  job_div += '<button class="btn btn form-control form-inline btn-danger remove_button" type="button">Remove</button>';
  job_div += '</div>';
  $('#WORK_DIV').append(job_div);
  job_ctr += 1;
}

function save(){
  var resume_JSON = {};
  resume_JSON.date_modified = new Date();
  resume_JSON.name = $('#NAME').val();
  resume_JSON.location = $('#LOCATION').val();
  resume_JSON.email = $('#EMAIL').val();
  resume_JSON.website = $('#WEBSITE').val();
  resume_JSON.github = $('#GITHUB').val();
  resume_JSON.linkedin = $('#LINKEDIN').val();
  resume_JSON.Education = [];

  //add degrees
  $('.DEGREE').each(function(){
    var deg = {};
    deg.degree = $(this).find('.DEGREE_DEGREE').val();
    deg.Institution = $(this).find('.DEGREE_INSTITUTION').val();
    deg['Cumulative GPA'] = $(this).find('.DEGREE_GPA').val();
    resume_JSON.Education.push(deg);
  });

  //add knowledge 
  resume_JSON.Knowledge = [];
  $('.KNOWLEDGE_SKILL').each(function(){
    resume_JSON.Knowledge.push($(this).val());
  });

  //add Programming Languages 
  resume_JSON['Programming Languages'] = [];
  $('.PROGRAMMING_LANGUAGE').each(function(){
    resume_JSON['Programming Languages'].push($(this).val());
  });

  //add Frameworks 
  resume_JSON['Frameworks'] = [];
  $('.FRAMEWORK').each(function(){
    resume_JSON['Frameworks'].push($(this).val());
  });

  //add Databases 
  resume_JSON['Database'] = {};
  $('.DBTYPE').each(function(index,val){
    var dbtypeName = $(this).val();
    var dbClass = $(this).attr('data-id');
    resume_JSON['Database'][dbtypeName] = [] ;
    $('.' + dbClass).each(function(index, val){
      resume_JSON['Database'][dbtypeName].push($(this).val());
    });
  });

  //add Operating Systems 
  resume_JSON['Operating Systems'] = [];
  $('.OS').each(function(){
    resume_JSON['Operating Systems'].push($(this).val());
  });

  //add Class Projects 
  resume_JSON['Class Projects'] = [];
  $('.CPROJ').each(function(){
    resume_JSON['Class Projects'].push($(this).val());
  });

  //add Research 
  resume_JSON.Research = [];
  $('.RSCH').each(function(){
    resume_JSON.Research.push($(this).val());
  });

  //add Personal Projects 
  resume_JSON['Personal Projects'] = [];
  $('.PPROJ').each(function(){
    resume_JSON['Personal Projects'].push($(this).val());
  });

  //add work history 
  resume_JSON['Work Experience'] = [];
  $('.WORK_HISTORY').each(function(){
    var job = {};
    job.Employer = $(this).find('.JOB_EMPLOYER').val();
    job.from= $(this).find('.JOB_FROM').val();
    job.to = $(this).find('.JOB_TO').val();
    job.Position = $(this).find('.JOB_TITLE').val();
    job.Duties = $(this).find('.JOB_DUTIES').val();
    resume_JSON['Work Experience'].push(job);
  });

  console.log(JSON.stringify(resume_JSON, null, 2));
  display_resume(resume_JSON,true);

  /*
  var editing_page = $("#EDIT").html();

  $.ajax({
    type: 'POST',
    // Provide correct Content-Type, so that Flask will know how to process it.
    contentType: 'application/json',
    // Encode your data as JSON.
    data: JSON.stringify(resume_JSON),
    // This is the type of data you're expecting back from the server.
    dataType: 'html',
    url: 'preview',
    success: function (e) {
      $('#EDIT').html(e)
      console.log(e);
    }
  });
  //console.log(editing_page);
*/
}
