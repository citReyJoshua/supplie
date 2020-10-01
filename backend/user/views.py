from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import CustomerRegistrationForm
from .models import Customer
from .choices import CHOICES_STATUS as status_choices, CHOICES_GENDER as gender_choices


class CustomerView(View):

    def get(self, request):
        customers = Customer.objects.all()  # pylint: disable=no-member
        context = {
            'customers': customers,
            'status_choices': status_choices,
            'gender_choices': gender_choices,
        }
        return render(request, 'customer/index.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btndelete' in request.POST:
                id = request.POST.get("btndelete")
                Customer.objects.get(id=id).delete()

            elif 'btnupdate' in request.POST:
                first_name = request.POST.get('first_name')
                middle_name = request.POST.get('middle_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                phone_number = request.POST.get('phone_number')
                profile_pic = request.POST.get('profile_pic')
                birthdate = request.POST.get('birthdate')
                birthplace = request.POST.get('birthplace')
                status = request.POST.get('status')
                gender = request.POST.get('gender')
                no_of_children = request.POST.get('no_of_children')

                # address fields
                brgy = request.POST.get('brgy')
                province = request.POST.get('province')
                city = request.POST.get('city')
                country = request.POST.get('country')
                zip_code = request.POST.get('zip_code')

                # spouse fields
                spouse_first_name = request.POST.get('spouse_first_name')
                spouse_last_name = request.POST.get('spouse_last_name')
                spouse_occupation = request.POST.get('spouse_occupation')

                # parent's fields
                father_first_name = request.POST.get('father_first_name')
                father_last_name = request.POST.get('father_last_name')
                father_occupation = request.POST.get('father_occupation')
                mother_first_name = request.POST.get('mother_first_name')
                mother_last_name = request.POST.get('mother_last_name')
                mother_occupation = request.POST.get('mother_occupation')

                height = request.POST.get('height')
                weight = request.POST.get('weight')
                religion = request.POST.get('weight')

                id = request.POST.get('btnupdate')
                Customer.objects.filter(id=id).update(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    profile_pic=profile_pic,
                    birthdate=birthdate,
                    birthplace=birthplace,
                    status=status,
                    gender=gender,
                    no_of_children=no_of_children,
                    brgy=brgy,
                    province=province,
                    city=city,
                    country=country,
                    zip_code=zip_code,
                    spouse_first_name=spouse_first_name,
                    spouse_last_name=spouse_last_name,
                    spouse_occupation=spouse_occupation,
                    father_first_name=father_first_name,
                    father_last_name=father_last_name,
                    father_occupation=father_occupation,
                    mother_first_name=mother_first_name,
                    mother_last_name=mother_last_name,
                    mother_occupation=mother_occupation,
                    height=height,
                    weight=weight,
                    religion=religion,
                )

        # bug : open gihapon ang modal ig redirect
        return redirect('/customer/')


class CustomerRegistrationView(View):

    def get(self, request):
        context = {
            'status_choices': status_choices,
            'gender_choices': gender_choices,
        }
        return render(request, 'registration/customer/index.html', context)

    def post(self, request):
        form = CustomerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/customer/')

        return HttpResponse(form.errors)


class LandingPage(View):

    def get(self, request):
        return render(request, 'landingpage/index.html')
