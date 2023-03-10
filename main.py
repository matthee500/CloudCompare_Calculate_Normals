import os
import subprocess


def cloud_compare_ss(direct, cc):
    ss_1 = 1
    sor_processed_directory = direct + '\\processed'
    if not os.path.exists(sor_processed_directory):
        os.makedirs(sor_processed_directory)

    for filename in os.listdir(direct):
        file = os.path.join(direct, filename)
        if os.path.isfile(file):
            if file.endswith('.e57'):
                cc_saved = sor_processed_directory + '\\' + 'sor' + str(ss_1) + '.e57'
                subprocess.check_call([cc, '-SILENT', '-NO_TIMESTAMP', '-AUTO_SAVE', 'OFF', '-C_EXPORT_FMT', 'E57',
                                       '-COMPUTE_NORMALS', '-O', '-GLOBAL_SHIFT', 'AUTO', file,
                                       '-DROP_GLOBAL_SHIFT', '-SAVE_CLOUDS', 'FILE', cc_saved], shell=True)
                ss_1 += 1


if __name__ == '__main__':
    directory = input('Input directory containing e57s: ')
    cloud_compare = r'C:\Program Files\CloudCompare\CloudCompare.exe'
    cloud_compare_ss(directory, cloud_compare)
