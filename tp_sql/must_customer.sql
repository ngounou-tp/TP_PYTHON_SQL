use classicmodels;
select * from payments;
SELECT customerName, count(customers.customerNumber) as qte, amount  FROM customers
inner join payments on customers.customerNumber = payments.customerNumber
GROUP BY payments.customerNumber
ORDER BY nbreAchat DESC;