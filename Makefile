##
## EPITECH PROJECT, 2017
## project name
## File description:
## Makefile for project name
##

SRC	=	main.c

OBJ	=	$(SRC:.cpp=.o)

CFLAGS	=	-Wall -Wextra

LIB	=	-lm -L./lib/my -lmy

NAME	=	

all	:	$(NAME)

$(NAME)	:	$(OBJ)
		make lib
		gcc -o $(NAME) $(OBJ) $(LIB)

lib	:	lib/my/Makefile	lib/graph/Makefile
		make -C lib/my
		make -C lib/graph

clean	:
		rm -f $(OBJ) *~ *#*
		make clean -C lib/my
		make clean -C lib/graph

fclean	:	clean
		rm -f $(NAME)
		make fclean -C lib/my
		make fclean -C lib/graph

re	:	fclean	all

.PHONY	:	all	lib	clean	fclean	re
