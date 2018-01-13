##
## EPITECH PROJECT, 2017
## 105torus
## File description:
## Makefile for 105torus
##

NAME	=	105torus

all	:	$(NAME)

$(NAME)	:	
		cp torus.py $(NAME)

fclean	:
		rm -f $(NAME)

re	:	fclean	all

.PHONY	:	all	fclean	re
