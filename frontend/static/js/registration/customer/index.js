$(()=>{
    $('.step-trigger').click((e)=>{

        $('.step.active').removeClass('active')
        let aria = "";
        if(e.target.tagName==='SPAN'){
            aria = e.target.parentNode.getAttribute('aria-controls')
            e.target.parentNode.parentNode.classList.add('active')
        }
        else{
            aria = e.target.getAttribute('aria-controls')
            e.target.parentNode.classList.add('active')
        }
        
        $('.bs-stepper-pane.active').removeClass('active')

        $('#'+aria).addClass('active')
        
    })

})
const personalInformationNext = () => {
$(()=>{
    $('.step.active').removeClass('active');
    $('#educational-background-part-trigger').parent().addClass('active');
    $('.bs-stepper-pane.active').removeClass('active')
    $('#educational-background-part').addClass('active');
})
}

const educationalBackgroundPrev = () => {
$(()=>{
    $('.step.active').removeClass('active');
    $('#personal-information-part-trigger').parent().addClass('active');
    $('.bs-stepper-pane.active').removeClass('active')
    $('#personal-information-part').addClass('active');
})
}

const educationalBackgroundNext = () => {
$(()=>{
    $('.step.active').removeClass('active');
    $('#professional-background-part-trigger').parent().addClass('active');
    $('.bs-stepper-pane.active').removeClass('active')
    $('#professional-background-part').addClass('active');
})
}

$(()=>{
    $('#step1-pagination').click((e)=>{
        if(e.target.tagName!=="UL"&&e.target.tagName!=="DIV"){
            let x=e.target.textContent
            if(x==='Previous'){
                x=$('#step1-pagination .page-item.active')[0].children[0].textContent
                if(parseInt(x)>1){
                    $('#step1-page-1').hide()
                    $('#step1-page-2').hide()
                    $('#step1-page-3').hide()
                    let temp = parseInt(x)-1
                    $('#step1-page-'+temp).show()
                    $('#step1-pagination .page-item.active').removeClass('active')
                    $('#step1-pagination .page-item')[parseInt(x)-1].classList.add('active')
                    
                }
            }
            else if(x==='Next'){
                x=$('#step1-pagination .page-item.active')[0].children[0].textContent
                if(parseInt(x)<3){
                    $('#step1-page-1').hide()
                    $('#step1-page-2').hide()
                    $('#step1-page-3').hide()
                    let temp = parseInt(x)+1
                    $('#step1-page-'+temp).show()
                    $('#step1-pagination .page-item.active').removeClass('active')
                    $('#step1-pagination .page-item')[parseInt(x)+1].classList.add('active')
                }
            }
            else{
                $('#step1-page-1').hide()
                $('#step1-page-2').hide()
                $('#step1-page-3').hide()
    
                $('#step1-page-'+x).show()
    
                $('#step1-pagination .page-item.active').removeClass('active')
                e.target.parentNode.classList.add('active')
    
            }
            // console.log(e.target)
        }
    })
})

$(()=>{
    $('#step2-pagination').click((e)=>{
        if(e.target.tagName!=="UL"&&e.target.tagName!=="DIV"){
            let x=e.target.textContent
            if(x==='Previous'){
                x=$('#step2-pagination .page-item.active')[0].children[0].textContent
                if(parseInt(x)>1){
                    $('#step2-page-1').hide()
                    $('#step2-page-2').hide()
                    $('#step2-page-3').hide()
                    $('#step2-page-4').hide()
                    $('#step2-page-5').hide()
                    let temp = parseInt(x)-1
                    $('#step2-page-'+temp).show()
                    $('#step2-pagination .page-item.active').removeClass('active')
                    $('#step2-pagination .page-item')[parseInt(x)-1].classList.add('active')
                }
            }
            else if(x==='Next'){
                x=$('#step2-pagination .page-item.active')[0].children[0].textContent
                if(parseInt(x)<5){
                    $('#step2-page-1').hide()
                    $('#step2-page-2').hide()
                    $('#step2-page-3').hide()
                    $('#step2-page-4').hide()
                    $('#step2-page-5').hide()
                    let temp = parseInt(x)+1
                    $('#step2-page-'+temp).show()
                    $('#step2-pagination .page-item.active').removeClass('active')
                    $('#step2-pagination .page-item')[parseInt(x)+1].classList.add('active')
                }
            }
            else{
                $('#step2-page-1').hide()
                $('#step2-page-2').hide()
                $('#step2-page-3').hide()
                $('#step2-page-4').hide()
                $('#step2-page-5').hide()

                $('#step2-page-'+x).show()
    
                $('#step2-pagination .page-item.active').removeClass('active')
                e.target.parentNode.classList.add('active')
    
            }
            // console.log(e.target)
        }
    })
})