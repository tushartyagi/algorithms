#lang racket

(struct node (value parent left right) #:mutable #:transparent)
(define (create-node v (p null) (l null) (r null))
  (node v p l r))

(define (inorder-walk tree)
  (if (null? tree)
      ""
      (begin
        (inorder-walk (node-left tree))
        (print (node-value tree))
        (inorder-walk (node-right tree)))))


(define (insert-node tree n)
  (cond ((null? tree) n)
        ((<= (node-value n) (node-value tree))
         (if (null? (node-left n))
             (begin
               (set-node-left! tree n)
               (set-node-parent! n tree))
             (insert-node (node-left tree) n)))
        ((> (node-value n) (node-value tree))
         (if (null? (node-right n))
             (begin
               (set-node-right! tree n)
               (set-node-parent! n tree))
             (insert-node (node-right tree) n)))))
