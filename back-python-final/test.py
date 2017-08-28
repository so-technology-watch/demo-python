import unittest
import datetime

from entities.Author import Author
from services import Author_service as commons_author_service

from entities.Badge import Badge
from services import Badge_service as commons_badge_service

from entities.Book import Book
from services import Book_service as commons_book_service

from entities.BookOrder import BookOrder
from services import BookOrder_service as commons_bookorder_service

from entities.Country import Country
from services import Country_service as commons_country_service

from entities.Customer import Customer
from services import Customer_service as commons_customer_service

from entities.Employee import Employee
from services import Employee_service as commons_employee_service

from entities.Publisher import Publisher
from services import Publisher_service as commons_publisher_service

from entities.Shop import Shop
from services import Shop_service as commons_shop_service

from entities.Synopsis import Synopsis
from services import Synopsis_service as commons_synopsis_service

from entities.Workgroup import Workgroup
from services import Workgroup_service as commons_workgroup_service


from commons.UnitTest.Author_unit_test_ import TestDaoAuthor
from commons.UnitTest.Badge_unit_test_ import TestDaoBadge
from commons.UnitTest.Book_unit_test_ import TestDaoBook
from commons.UnitTest.BookOrder_unit_test_ import TestDaoBookOrder
from commons.UnitTest.BookOrderItem_unit_test_ import TestDaoBookOrderItem
from commons.UnitTest.Country_unit_test_ import TestDaoCountry
from commons.UnitTest.Customer_unit_test_ import TestDaoCustomer
from commons.UnitTest.Employee_unit_test_ import TestDaoEmployee
from commons.UnitTest.EmployeeGroup_unit_test_ import TestDaoEmployeeGroup
from commons.UnitTest.Publisher_unit_test_ import TestDaoPublisher
from commons.UnitTest.Review_unit_test_ import TestDaoReview
from commons.UnitTest.Shop_unit_test_ import TestDaoShop
from commons.UnitTest.Synopsis_unit_test_ import TestDaoSynopsis
from commons.UnitTest.Workgroup_unit_test_ import TestDaoWorkgroup

author_service = commons_author_service.AuthorService()
badge_service = commons_badge_service.BadgeService()
book_service = commons_book_service.BookService()
bookorder_service = commons_bookorder_service.BookOrderService()
country_service = commons_country_service.CountryService()
customer_service = commons_customer_service.CustomerService()
employee_service = commons_employee_service.EmployeeService()
publisher_service = commons_publisher_service.PublisherService()
shop_service = commons_shop_service.ShopService()
synopsis_service = commons_synopsis_service.SynopsisService()
workgroup_service = commons_workgroup_service.WorkgroupService()


if __name__ == '__main__':

    # --- Init Author
    init_author = Author()
    init_author.id = 100
    init_author.firstName = "AAAAAAAAA"
    init_author.lastName = "AAAAAAAAA"

    # --- Init Badge
    init_badge = Badge()
    init_badge.badgeNumber = 100
    init_badge.authorizationLevel = 111111111
    init_badge.endOfValidity = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")

    # --- Init Book
    init_book = Book()
    init_book.id = 100
    init_book.publisherId = 100	
    init_book.authorId = 100	
    init_book.isbn = "AAAAAAAAA"
    init_book.title = "AAAAAAAAA"
    init_book.price = 111111111
    init_book.quantity = 111111111
    init_book.discount = 111111111
    init_book.availability = 111111111
    init_book.bestSeller = 111111111

    # --- Init BookOrder
    init_bookorder = BookOrder()
    init_bookorder.id = 100
    init_bookorder.shopCode = "AAA"
    init_bookorder.customerCode = "AAA"
    init_bookorder.employeeCode = "AAA"
    init_bookorder.date = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")
    init_bookorder.state = 111111111

    # --- Init Country
    init_country = Country()
    init_country.code = "AAA"
    init_country.name = "AAAAAAAAA"

    # --- Init Customer
    init_customer = Customer()
    init_customer.code = "AAA"
    init_customer.countryCode = "AAA"
    init_customer.firstName = "AAAAAAAAA"
    init_customer.lastName = "AAAAAAAAA"
    init_customer.login = "AAAAAAAAA"
    init_customer.password = "AAAAAAAAA"
    init_customer.age = 111111111
    init_customer.city = "AAAAAAAAA"
    init_customer.zipCode = 111111111
    init_customer.phone = "AAAAAAAAA"
    init_customer.reviewer = 111111111

    # --- Init Employee
    init_employee = Employee()
    init_employee.code = "AAA"
    init_employee.shopCode = "AAA"
    init_employee.firstName = "AAAAAAAAA"
    init_employee.lastName = "AAAAAAAAA"
    init_employee.manager = 111111111
    init_employee.badgeNumber = None
    init_employee.email = "AAAAAAAAA"

    # --- Init Publisher
    init_publisher = Publisher()
    init_publisher.code = 100
    init_publisher.countryCode = "AAA"
    init_publisher.name = "AAAAAAAAA"
    init_publisher.email = "AAAAAAAAA"
    init_publisher.contact = "AAAAAAAAA"
    init_publisher.city = "AAAAAAAAA"
    init_publisher.zipCode = 111111111
    init_publisher.phone = "AAAAAAAAA"

    # --- Init Shop
    init_shop = Shop()
    init_shop.code = "AAA"
    init_shop.name = "AAAAAAAAA"
    init_shop.address1 = "AAAAAAAAA"
    init_shop.address2 = "AAAAAAAAA"
    init_shop.zipCode = 111111111
    init_shop.city = "AAAAAAAAA"
    init_shop.countryCode = "AAA"
    init_shop.phone = "AAAAAAAAA"
    init_shop.email = "AAAAAAAAA"
    init_shop.executive = None

    # --- Init Synopsis
    init_synopsis = Synopsis()
    init_synopsis.bookId = 100
    init_synopsis.synopsis = "AAAAAAAAA"

    # --- Init Workgroup
    init_workgroup = Workgroup()
    init_workgroup.id = 100
    init_workgroup.name = "AAAAAAAAA"
    init_workgroup.description = "AAAAAAAAA"
    init_workgroup.creationDate = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")

    author_service.insert(init_author)
    badge_service.insert(init_badge)
    country_service.insert(init_country)
    workgroup_service.insert(init_workgroup)
    customer_service.insert(init_customer)
    publisher_service.insert(init_publisher)
    synopsis_service.insert(init_synopsis)
    book_service.insert(init_book)
    employee_service.insert(init_employee)
    shop_service.insert(init_shop)
    bookorder_service.insert(init_bookorder)

    unittest.main()
