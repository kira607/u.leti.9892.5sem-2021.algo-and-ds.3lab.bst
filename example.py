from bst import BST


def main():
    bst = BST(10, 10, 5, 3, 20, 15, 70, 30, 8, 7, 4, 9, 2, 2)
    print(bst)
    print(f'height: {bst.height}')
    print(f'bft: {tuple(bst.bft())}')
    print(f'dft inorder: {tuple(bst.dft("inorder"))}')
    print(f'dft preorder: {tuple(bst.dft("preorder"))}')
    print(f'dft postorder: {tuple(bst.dft("postorder"))}')


if __name__ == '__main__':
    main()
