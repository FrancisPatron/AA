#lang racket

(define (mergesort x )
  (cond ((null? x) x)
        ((null? (cdr x)) x)
        (else (mergelist (mergesort (oddlist x)) (mergesort (evenlist x))
                         ))))

(define (mergelist L R)
  (cond ((null? L) R)
        ((null? R) L)
        ((<= (car L) (car R))
         (cons (car L) (mergelist (cdr L) R)))
        (else (cons (car R) (mergelist L (cdr R))))))

(define (oddlist x)
  (cond ((null? x) x)
        ((null? (cdr x)) x)
        (else (cons (car x) (oddlist (cdr (cdr x)))))))

(define (evenlist x)
  (cond ((null? x) x)
        ((null? (cdr x)) '())
        (else (cons (car (cdr x)) (evenlist (cdr (cdr x)))))))
