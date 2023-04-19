import pytest
from selene import browser, have
import os


def test_entry_form(browser_management):
    browser.open('/automation-practice-form')
    browser.element('[class=main-header]').should(have.text('Practice Form'))
    browser.element('#firstName').type('Nikita')
    browser.element('#lastName').type('Troshenko')
    browser.element('#userEmail').type('gferrerewrrn@mail.ru')
    browser.element('.custom-control [for=gender-radio-1]').click()
    browser.element('#userNumber').type('9638460094')
    browser.element('#dateOfBirthInput').press()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value="5"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="1994"]').click()
    browser.element('.react-datepicker__day--028').click()
    browser.element('#subjectsInput').send_keys('History').press_enter()
    browser.element('.custom-control [for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/1.jpg')
    browser.element('#currentAddress').type('Perm')
    browser.element('#react-select-3-input').type('Uttar').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('#submit').press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tbody tr') \
        .should(have.exact_texts('Student Name Nikita Troshenko', 'Student Email gferrerewrrn@mail.ru', 'Gender Male',
                                 'Mobile 9638460094', 'Date of Birth 28 June,1994',
                                 'Subjects History', 'Hobbies Sports', 'Picture 1.jpg',
                                 'Address Perm', 'State and City Uttar Pradesh Agra'))
    browser.element('#closeLargeModal').click()
