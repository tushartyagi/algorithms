#lang racket

(define v (vector 16 4 10 14 7 9 3 2 8 1))
(define v2 (vector 14 8 10 2 7 9 3 1 4 16))

(define (heapsort v)
  (define (left i) (+ (* 2 i) 1))
  (define (right i) (+ (* 2 i) 2))
  (define (parent i) (floor (/ (- i 1) 2)))
  (define size (vector-length v))
  (define heapsize (- size 1))
  
  (define (heapify-node i);; node i is larger than both children?
    (let ((l (left i))
          (r (right i))
          (largest i))
      (cond ((and (< l heapsize) (> (vector-ref v l) (vector-ref v largest)))
             (set! largest l))
            ((and (< r heapsize) (> (vector-ref v r) (vector-ref v largest)))
             (set! largest r)))
      (if (not (equal? i largest))
          (begin
            (exchange i largest)
            (heapify-node largest))
          #t)))
  
  (define (heapify-tree)
    (for ((i (in-range (floor (/ size 2)) -1 -1)))
      (heapify-node i)))

  (define (exchange a b)
    (let ((va (vector-ref v a))
          (vb (vector-ref v b)))
      (vector-set! v a vb)
      (vector-set! v b va)))
  
  (define (sort)
    (begin
      (heapify-tree)
      (print v)
      (for ((i (in-range (- size 1) 1 -1)))
        (exchange 0 i)
        (set! heapsize (- heapsize 1))
        (heapify-node 0)))
    v)
  
  (sort))


