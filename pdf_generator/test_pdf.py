from pdf_generator.generator import generate_pdf


sample_report = {

"patient":
{
"id":1,
"name":"Test Patient"
},


"scan":
{
"modality":"MR",
"file_name":"brain.jpg"
},


"ai_result":
{
"prediction":"glioma",
"confidence":99.91,
"gradcam_path":"gradcam.jpg"
},


"medical_report":
{
"finding":
"MRI findings suggest Glioma",

"severity":
"High",

"recommendation":
"Consult neurologist"
},


"simplified_report":
{
"explanation":
"The scan may show a type of brain tumor.",

"summary":
"Further evaluation is recommended."
},


"readability":
{
"score":85,
"level":"Easy"
}

}



generate_pdf(

sample_report,

"report.pdf"

)


print(
"PDF created"
)